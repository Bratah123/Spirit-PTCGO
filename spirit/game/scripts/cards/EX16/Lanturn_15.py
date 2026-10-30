from spirit.game.data_utils import Triggers, Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import energy_grounding, lightning_strike

card = PokemonCardDef(
    guid="315d0cd7-57a9-563f-9a66-8239647bfb19",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Energy Grounding",
            game_text="Once during your opponent's turn, when any of your Pok\u00e9mon is Knocked Out by your opponent's attacks, you may use this power. Choose a basic Energy card discarded from the Knocked Out Pok\u00e9mon and attach it to Lanturn. You can't use more than 1 Energy Grounding Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=energy_grounding,
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning Energy attached to Lanturn. If you do, this attack's base damage is 90 instead of 50.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=lightning_strike(100),
        ),
    ],
)