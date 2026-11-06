from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.ecard import has_bench
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="a877f2e2-efcf-5d67-be2a-6ca8f282ac03",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Teleport",
            game_text="Switch Exeggutor with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            condition=has_bench,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Big Eggsplosion",
            game_text="Flip a number of coins equal to the number of Energy attached to Exeggutor. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=20),
        ),
    ],
)
