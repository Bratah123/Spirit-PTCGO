from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dm import (
    explosive_jet,
)

card = PokemonCardDef(
    guid="be18cf41-d9be-5af8-b7fa-c9ee1c4d775d",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=776,
    abilities=[
        Attack(
            title="Explosive Jet",
            game_text="Discard any amount of Fire Energy from your Pok\u00e9mon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            damage_operator="x",
            effect=explosive_jet,
        ),
    ],
)