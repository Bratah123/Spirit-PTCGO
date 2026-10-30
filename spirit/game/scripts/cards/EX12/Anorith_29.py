"""STUB: effect not implemented — do not guess mechanics.
Anorith (EX12 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import stretch_claws_react, search_to_bench_named


card = PokemonCardDef(
    guid="e496735b-4e1e-51c7-8a36-9d1d2b728fb1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith",
    searchable_by=["Anorith", "Stage 1", "Anorith"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ClawFossil.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Influence",
            game_text="Search your deck for Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith and put up to 2 of them onto your Bench. Shuffle your deck afterward. Treat the new Benched Pok\u00e9mon as Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_bench_named('Omanyte', 'Kabuto', 'Aerodactyl', 'Lileep', 'Anorith', count=2, prompt='Choose up to 2 of Omanyte, Kabuto, Aerodactyl, Lileep, or Anorith to put onto your Bench.'),
        ),
        Attack(
            title="Stretch Claws",
            game_text="If Anorith has any React Energy cards attached to it, this attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=stretch_claws_react(20),
        ),
    ],
)