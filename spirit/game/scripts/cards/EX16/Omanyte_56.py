"""STUB: effect not implemented — do not guess mechanics.
Omanyte (EX16 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import search_to_bench_named


card = PokemonCardDef(
    guid="b55206a7-2858-522c-bde1-f2d78ea33589",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Influence",
            game_text="Search your deck for Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith and put up to 2 of them onto your Bench. Shuffle your deck afterward. Treat the new Benched Pok\u00e9mon as Basic Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=search_to_bench_named('Omanyte', 'Kabuto', 'Aerodactyl', 'Lileep', 'Anorith', count=2, prompt='Choose up to 2 of Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith to put onto your Bench.'),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)