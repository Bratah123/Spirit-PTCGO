"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Crawdaunt (EX4 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import aqua_reverse, deep_impact

card = PokemonCardDef(
    guid="4c23ec59-8282-5dac-99c9-151284b91c41",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCrawdaunt.Name",
    display_name="Team Aqua's Crawdaunt",
    searchable_by=["Team Aqua's Crawdaunt", "Stage 1", "TeamAquasCrawdaunt"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCorphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Aqua Reverse",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon that has Team Magma in its name and switch it with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=aqua_reverse(),
        ),
        Attack(
            title="Deep Impact",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=deep_impact(),
        ),
    ],
)