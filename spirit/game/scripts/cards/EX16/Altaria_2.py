"""STUB: effect not implemented — do not guess mechanics.
Altaria (EX16 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import altaria_synergy_heal_between_turns, shuffle_random_from_opponent_hand


card = PokemonCardDef(
    guid="f29fccdb-f3a9-5379-9f5a-098f48ecf462",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Synergy Effect",
            game_text="If Drake's Stadium is in play, remove 1 damage counter from Altaria between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=altaria_synergy_heal_between_turns(),
        ),
        Attack(
            title="Surprise",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=shuffle_random_from_opponent_hand(),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)