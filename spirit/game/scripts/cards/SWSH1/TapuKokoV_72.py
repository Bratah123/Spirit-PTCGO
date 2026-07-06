from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ecef3f1d-c12c-50f6-85ed-e869f10f9116",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoV.Name",
    display_name="Tapu Koko V",
    searchable_by=["Tapu Koko V", "Basic", "V", "TapuKokoV"],
    subtypes=["Basic", "V"],
    collector_number=72,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=785,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)