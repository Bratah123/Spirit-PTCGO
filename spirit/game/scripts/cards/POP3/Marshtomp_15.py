from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="e8352bf7-4cd0-5965-b3e4-4bf81c821c83",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    display_name="Marshtomp",
    searchable_by=["Marshtomp", "Stage 1", "Marshtomp"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="POP3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    family_id=259,
    abilities=[
        Attack(
            title="Mud Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Double-edge",
            game_text="Marshtomp does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)
