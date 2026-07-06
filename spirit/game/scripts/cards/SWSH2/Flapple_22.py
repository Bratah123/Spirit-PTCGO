from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da729e0f-309f-50ef-aafe-9c34630e6e10",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Apple Drop",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If you placed any damage counters in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)