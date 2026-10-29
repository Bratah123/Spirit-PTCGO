from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm3 import gutsy_hammer


card = PokemonCardDef(
    guid="b4daffff-25ab-590b-9424-6a43eace8ee2",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1", "Crabominable"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
    abilities=[
        Attack(
            title="Gutsy Hammer",
            game_text="This Pok\u00e9mon does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=80,
            effect=gutsy_hammer,
        ),
        Attack(
            title="Double Stomp",
            game_text="Flip 2 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, bonus_per_heads=40),
        ),
    ],
)
