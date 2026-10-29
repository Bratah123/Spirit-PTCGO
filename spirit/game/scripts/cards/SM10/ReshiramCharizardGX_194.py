from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import onix_rage

from spirit.game.card_effects.sm10 import (
    double_blaze_gx,
)

card = PokemonCardDef(
    guid="4084b5d1-0398-5e79-8276-2a94ae4e9a61",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramCharizardGX.Name",
    display_name="Reshiram & Charizard-GX",
    searchable_by=["Reshiram & Charizard-GX", "Basic", "TAG TEAM", "GX", "ReshiramCharizardGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=194,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=onix_rage,
        ),
        Attack(
            title="Flare Strike",
            game_text="This Pok\u00e9mon can't use Flare Strike during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            locks_next_turn=True
        ),
        Attack(
            title="Double Blaze-GX",
            game_text="If this Pok\u00e9mon has at least 3 extra Fire Energy attached to it (in addition to this attack's cost), this attack does 100 more damage, and this attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 3},
            damage=200,
            damage_operator="+",
            effect=double_blaze_gx
        ),
    ],
)