"""STUB: effect not implemented — do not guess mechanics.
Rhydon (EX5 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import hyper_tail, power_diffusion_passive

card = PokemonCardDef(
    guid="7cc0ac6f-203c-50f9-9ce3-de81a1fa4958",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1", "Rhydon"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Ability(
            title="Power Diffusion",
            game_text="As long as Rhydon is your Active Pok\u00e9mon, prevent all damage done by attacks to all of your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=power_diffusion_passive(),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Hyper Tail",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Powers or Pok\u00e9-Bodies, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=hyper_tail(50, 20),
        ),
    ],
)