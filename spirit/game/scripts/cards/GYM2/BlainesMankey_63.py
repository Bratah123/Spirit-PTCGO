from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import pranks


card = PokemonCardDef(
    guid="d2874d19-358f-500c-8153-8b03a55d18d3",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesMankey.Name",
    display_name="Blaine's Mankey",
    searchable_by=["Blaine's Mankey", "Basic", "BlainesMankey"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Pranks",
            game_text="Flip a coin. If heads, choose a card from your opponent's discard pile and put it on top of his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pranks,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)
