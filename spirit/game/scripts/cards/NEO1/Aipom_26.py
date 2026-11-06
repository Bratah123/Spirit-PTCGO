from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import pilfer


card = PokemonCardDef(
    guid="96485596-a083-5396-a008-dad4d0029643",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=190,
    abilities=[
        Attack(
            title="Pilfer",
            game_text="Shuffle Aipom and all cards attached to it into your deck. Flip a coin. If heads, shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pilfer,
        ),
        Attack(
            title="Tail Rap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)
