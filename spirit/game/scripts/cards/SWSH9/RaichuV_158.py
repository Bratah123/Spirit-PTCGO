from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d2cd69b4-9c28-5ef4-9bf2-4b0f12c2cf89",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuV.Name",
    display_name="Raichu V",
    searchable_by=["Raichu V", "Basic", "V", "RaichuV"],
    subtypes=["Basic", "V"],
    collector_number=158,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=26,
    abilities=[
        Attack(
            title="Fast Charge",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dynamic Spark",
            game_text="You may discard any amount of Lightning Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)