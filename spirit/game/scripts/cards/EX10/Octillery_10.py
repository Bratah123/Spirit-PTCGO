"""STUB: effect not implemented — do not guess mechanics.
Octillery (EX10 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import suction_cups_no_retreat_passive, standing_by_boost

card = PokemonCardDef(
    guid="513dd1dd-080f-5bee-a43a-30bd9a33692c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Super Suction Cups",
            game_text="As long as Octillery is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't retreat.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=suction_cups_no_retreat_passive(),
        ),
        Attack(
            title="Standing By",
            game_text="Discard an Energy card attached to Octillery. During your next turn, Octillery's Pulse Blast attack's base damage is 120.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standing_by_boost("Pulse Blast", 120),
        ),
        Attack(
            title="Pulse Blast",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)