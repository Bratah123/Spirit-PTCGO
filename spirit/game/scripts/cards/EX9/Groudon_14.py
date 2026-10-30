"""STUB: effect not implemented — do not guess mechanics.
Groudon (EX9 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import eruption_damage

card = PokemonCardDef(
    guid="8248a2de-6179-589f-abd3-9e7b8191922e",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 40 damage plus 10 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
                        effect=eruption_damage(40, 10),
        ),
    ],
)