from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="9e0bdfb7-a8b8-52d4-af36-b30a02829f4c",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "MEGA", "EX", "MCharizardEX"],
    subtypes=["MEGA", "EX"],
    collector_number=13,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Crimson Dive",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3},
            damage=300,
            effect=recoil_attack(50),
        ),
    ],
)