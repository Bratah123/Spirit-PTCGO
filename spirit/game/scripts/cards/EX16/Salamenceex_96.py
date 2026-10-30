"""STUB: effect not implemented — do not guess mechanics.
Salamence ex (EX16 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import hydro_wave_discard_water_spread, volcanic_flame_mill5
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="93744565-031f-5bfe-95f6-03f2eea9efe5",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamenceex.Name",
    display_name="Salamence ex",
    searchable_by=["Salamence ex", "Stage 2", "ex", "Salamenceex"],
    subtypes=["Stage 2", "ex"],
    collector_number=96,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Volcanic Flame",
            game_text="Discard the top 5 cards from your deck.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=volcanic_flame_mill5(),
        ),
        Attack(
            title="Hydro Wave",
            game_text="Discard all Water Energy attached to Salamence ex. This attack does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=hydro_wave_discard_water_spread(30),
        ),
    ],
)