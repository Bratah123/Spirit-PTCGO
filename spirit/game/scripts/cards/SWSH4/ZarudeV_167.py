from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="99a969ba-e5ee-5e63-a00e-4335f4d5008b",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZarudeV.Name",
    display_name="Zarude V",
    searchable_by=["Zarude V", "Basic", "V", "ZarudeV"],
    subtypes=["Basic", "V"],
    collector_number=167,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Rising",
            game_text="You may attach up to 2 basic Energy cards from your hand to your Benched Pok\u00e9mon in any way you like. If you attached Energy to a Pok\u00e9mon in this way, heal all damage from that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)