from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached,
)


card = PokemonCardDef(
    guid="577c362a-aca4-538d-a263-a310ca1ce2bd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=147,
    set_code="ECARD3",
    rarity=Rarities.RareSecret,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Grass, Fire, or Psychic basic Energy card from your hand to Crobat, Crobat's type (color) becomes the same as that type of Energy until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.PSYCHIC,
            ),
        ),
        Attack(
            title="Poison Flame",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.BURNED, SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Squared Attack",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)
