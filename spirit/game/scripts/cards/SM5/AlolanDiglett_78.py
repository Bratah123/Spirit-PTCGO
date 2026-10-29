from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="4260dc37-927a-5b0d-be8a-706098d82077",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic", "AlolanDiglett"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=50,
    abilities=[
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 10 damage for each heads.",
            cost={},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(until_tails=True, per_heads=10),
        ),
    ],
)