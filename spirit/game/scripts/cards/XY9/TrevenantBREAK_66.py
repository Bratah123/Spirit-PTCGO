from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


card = PokemonCardDef(
    guid="fd5a1224-8387-5d6e-b0c6-b761f54ba11b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantBREAK.Name",
    display_name="Trevenant BREAK",
    searchable_by=["Trevenant BREAK", "BREAK", "TrevenantBREAK"],
    subtypes=["BREAK"],
    collector_number=66,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Silent Fear",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(3, 'each_opponent'),
        ),
    ],
)