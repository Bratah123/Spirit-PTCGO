from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.hf import happy_mime

card = PokemonCardDef(
    guid="1f9285e6-e026-5bfb-9b2b-80edc21e16be",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="HF",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title="Happy Mime",
            game_text="Each player draws a card.",
            cost={PokemonTypes.FAIRY: 1},
            effect=happy_mime,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.FAIRY: 2},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)
