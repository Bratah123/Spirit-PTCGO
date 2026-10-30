from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="5aa40113-ea05-50f2-a8f8-03fd50915b0b",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=195,
    abilities=[
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
        Attack(
            title="Whirlpool",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, choose 1 of them and discard it.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)
