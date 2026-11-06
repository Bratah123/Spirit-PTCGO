from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import pure_body_on_energy_attached


card = PokemonCardDef(
    guid="8abe54fc-7a18-5239-bf97-6f3241c1504b",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Pure Body",
            game_text="To attach a Water Energy card from your hand to Suicune, you must discard an Energy card attached to Suicune. (Attach the Water Energy, and then discard an Energy card from Suicune.)",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=pure_body_on_energy_attached(PokemonTypes.WATER),
        ),
        Attack(
            title="Hypno Wave",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage. If tails, this attack does 30 damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=condition_attack(
                flip=True,
                heads_bonus_damage=20,
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
    ],
)
