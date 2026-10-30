"""EX12 Legend Maker — Cursed Stone stadium.
"""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations, Triggers
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.ex import cursed_stone_between_turns


card = StadiumCardDef(
    guid="e8bf4f78-75fa-56e8-8cf1-386a6fe3710a",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedStone.Name",
    display_name="Cursed Stone",
    searchable_by=["Cursed Stone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Cursed Stone",
        game_text="At any time between turns, each player puts 1 damage counter on his or her Pokémon that has a Poké-Power.",
        ability_type=AbilityTypes.POKE_BODY,
        effect=cursed_stone_between_turns(),
        trigger=Triggers.BETWEEN_TURNS,
    ),
)
