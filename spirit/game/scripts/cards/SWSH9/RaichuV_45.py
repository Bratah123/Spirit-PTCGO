from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="363bf9c7-0376-53d1-913a-74d464f30b0f",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuV.Name",
    display_name="Raichu V",
    searchable_by=["Raichu V", "Basic", "V", "RaichuV"],
    subtypes=["Basic", "V"],
    collector_number=45,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
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