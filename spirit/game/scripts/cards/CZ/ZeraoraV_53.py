from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b68383ff-062f-5710-a4ab-d3c397c2be05",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    display_name="Zeraora V",
    searchable_by=["Zeraora V", "Basic", "V", "ZeraoraV"],
    subtypes=["Basic", "V"],
    collector_number=53,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            locks_next_turn=True,
        ),
    ],
)