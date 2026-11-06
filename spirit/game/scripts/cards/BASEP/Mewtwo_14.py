from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard


card = PokemonCardDef(
    guid="c97451c1-c781-5126-82dd-729446dd5128",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Choose up to 2 Energy cards from your discard pile and attach them to Mewtwo.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=attach_from_discard(count=2, minimum=0),
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
