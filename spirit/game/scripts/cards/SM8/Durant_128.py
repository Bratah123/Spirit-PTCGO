from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import knock_over
from spirit.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="ec13f698-338a-5f33-b8d0-83ea07d5bac0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=knock_over,
        ),
        Attack(
            title="Mountain Munch",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mill_attack(2),
        ),
    ],
)