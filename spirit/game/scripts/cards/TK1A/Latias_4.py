"""Latias (TK1A #4)."""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="c85acc91-87ce-5be1-88c1-f800bd82fccb",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="TK1A",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Attack(
            title="Dragon Dew",
            game_text="Remove 1 damage counter from 1 of your Pok\u00e9mon",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=heal_targets(10, scope="choice"),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
