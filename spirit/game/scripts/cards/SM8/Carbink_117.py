from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

from spirit.game.card_effects.sm8 import (
    diamond_gate,
)

card = PokemonCardDef(
    guid="56219c9b-8b4b-5154-a89b-612bc12367f5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Attack(
            title="Diamond Gate",
            game_text="Search your deck for a Supporter card and a Stadium card, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=diamond_gate
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)