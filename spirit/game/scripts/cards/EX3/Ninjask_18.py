"""STUB: effect not implemented — do not guess mechanics.
Ninjask (EX3 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import loose_shell_search, quick_touch

card = PokemonCardDef(
    guid="19eb1797-8ea7-59e8-b044-799f2efae463",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Loose Shell",
            game_text="Once during your turn, when you play Ninjask from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for Shedinja and put it onto your Bench. Treat the new Benched Pok\u00e9mon as a Basic Pok\u00e9mon. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=(Triggers.ON_PLAY, Triggers.ON_EVOLVE),
            # STUB: ability effect not implemented
            effect=loose_shell_search(),
        ),
        Attack(
            title="Quick Touch",
            game_text="You may switch Ninjask with 1 of your Benched Pok\u00e9mon. If you do, you may move any number of Grass Energy cards attached to Ninjask to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=quick_touch(),
        ),
    ],
)