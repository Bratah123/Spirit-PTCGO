from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4982ce9a-4bdd-5895-9974-d3c4895a1dcd",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuVMAX.Name",
    display_name="Mimikyu VMAX",
    searchable_by=["Mimikyu VMAX", "VMAX", "MimikyuVMAX"],
    subtypes=["VMAX"],
    collector_number=69,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MimikyuV.Name",
    family_id=778,
    abilities=[
        Attack(
            title="Ominous Numbers",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like. If you played Acerola's Premonition from your hand during this turn, place 13 damage counters instead.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Max Shadow",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)