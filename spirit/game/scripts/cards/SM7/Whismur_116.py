from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    bawl,
)
from spirit.game.card_effects.sm5 import go_second_first_turn

card = PokemonCardDef(
    guid="d1c358bc-9743-5e66-8c68-dfea6639d5e7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Bawl",
            game_text="You can use this attack only if you go second, and only on your first turn. Your opponent can't play any Trainer cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bawl,
            condition=go_second_first_turn,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)