from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_evolution_pokemon

card = PokemonCardDef(
    guid="4a6f95d4-106c-5327-a59b-915801c50f58",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogekissV.Name",
    display_name="Togekiss V",
    searchable_by=["Togekiss V", "Basic", "V", "TogekissV"],
    subtypes=["Basic", "V"],
    collector_number=140,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=468,
    abilities=[
        Attack(
            title="White Wind",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(active_is(is_evolution_pokemon), 70),
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)