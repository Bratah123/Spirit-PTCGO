from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8efb553b-cfee-5681-8e21-dfccb14ac5fe",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1", "Palossand"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Sink",
            game_text="Discard the top card of your opponent's deck. If this Pok\u00e9mon has a Cursed Shovel attached, discard 2 more cards from the top of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Super Absorption",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)