from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import condition_on_damaged


card = PokemonCardDef(
    guid="e9944d19-7de8-5e5b-80e1-35ddffa0c56d",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    display_name="Growlithe",
    searchable_by=["Growlithe", "Basic", "Growlithe"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Ability(
            title="Fire Veil",
            game_text="If Growlithe is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Growlithe is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=condition_on_damaged(SpecialConditions.BURNED),
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
