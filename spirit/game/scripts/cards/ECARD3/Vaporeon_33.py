from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import aqua_trick, self_healing_on_energy_attached


card = PokemonCardDef(
    guid="a9e3c5e5-629b-5a9a-8602-44de04128f68",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Self-healing",
            game_text="Whenever you attach a Water Energy card from your hand to Vaporeon, remove all Special Conditions affecting Vaporeon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=self_healing_on_energy_attached(PokemonTypes.WATER),
        ),
        Attack(
            title="Hypnosplash",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Aqua Trick",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and move it to 1 of your opponent's Benched Pok\u00e9mon. If your opponent has no Benched Pok\u00e9mon, ignore this effect.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=aqua_trick,
        ),
    ],
)
