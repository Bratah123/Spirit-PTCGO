from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="7e01c8e9-5ad8-5939-baef-afd0981e0977",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primarina.Name",
    display_name="Primarina",
    searchable_by=["Primarina", "Stage 2", "Primarina"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Disarming Voice",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Sparkling Aria",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=heal_attack(30),
        ),
    ],
)