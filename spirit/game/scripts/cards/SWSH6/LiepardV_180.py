from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="320309c8-237c-5a29-8572-cc01d205a5ae",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LiepardV.Name",
    display_name="Liepard V",
    searchable_by=["Liepard V", "Basic", "V", "LiepardV"],
    subtypes=["Basic", "V"],
    collector_number=180,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=510,
    abilities=[
        Ability(
            title="Hidden Claw",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Pok\u00e9mon Tool from a Pok\u00e9mon (yours or your opponent's).",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Ripper",
            game_text="You may put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=unimplemented,
        ),
    ],
)