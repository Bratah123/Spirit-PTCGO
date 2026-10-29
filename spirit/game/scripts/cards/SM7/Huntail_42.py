from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if, active_is
from spirit.game.session.effects import is_basic_pokemon


card = PokemonCardDef(
    guid="7c2fdd98-9ac4-5c64-a516-715bf4bbacda",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Huntail"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Dangerous Bite",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(active_is(is_basic_pokemon), 80),
        ),
    ],
)