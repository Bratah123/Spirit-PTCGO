from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.sm3 import crossing_cut_gx

from spirit.game.card_effects.sm8 import (
    is_benched_pokemon,
    phantom_winds,
)

card = PokemonCardDef(
    guid="c399ccfb-0b82-5cca-935d-f7b800edb205",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneGX.Name",
    display_name="Suicune-GX",
    searchable_by=["Suicune-GX", "Basic", "GX", "SuicuneGX"],
    subtypes=["Basic", "GX"],
    collector_number=200,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Phantom Winds",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may shuffle it and all cards attached to it into your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=phantom_winds,
            activation=Activations.ONCE_PER_TURN,
            condition=is_benched_pokemon,
        ),
        Attack(
            title="Cure Stream",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=debuff_defender_attacks(30),
        ),
        Attack(
            title="Brinicles-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=crossing_cut_gx,
        ),
    ],
)