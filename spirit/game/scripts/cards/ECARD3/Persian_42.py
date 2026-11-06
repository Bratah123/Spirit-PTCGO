from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import surprise_slash


card = PokemonCardDef(
    guid="02910e56-7607-5c3b-810f-9ba45bcfc52c",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Surprise Slash",
            game_text="Flip a coin. If heads, look at your opponent's hand. If he or she has any Trainer cards there, choose 1 of them. You opponent shuffles that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=surprise_slash,
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)
