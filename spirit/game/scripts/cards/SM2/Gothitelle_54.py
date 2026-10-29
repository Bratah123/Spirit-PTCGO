from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


from spirit.game.card_effects.attacks_common import count_energy, bonus_if


def _equal_energy(ctx):
    return count_energy()(ctx) == count_energy("defender")(ctx)


card = PokemonCardDef(
    guid="3d5bb200-6cb6-5c80-935f-84cf46158433",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Tractorbeam",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Link Blast",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached to them, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_equal_energy, 80),
        ),
    ],
)