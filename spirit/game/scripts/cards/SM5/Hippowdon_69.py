from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm5 import dust_cannon

card = PokemonCardDef(
    guid="b4328c45-7933-56b7-8e02-6ff2856ed265",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Dust Cannon",
            game_text="This attack does 10 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=dust_cannon,
        ),
    ],
)