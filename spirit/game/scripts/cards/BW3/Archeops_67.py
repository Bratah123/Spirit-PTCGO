from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.session.passives import Passive


class AncientPowerPassive(Passive):
    """Each player can't evolve Pokémon from hand."""

    def blocks_evolution(self, player_id, target, carrier):
        return True


card = PokemonCardDef(
    guid="c46546cf-1e8c-52e8-a10d-53b49941a0ec",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 1", "Archeops"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Ancient Power",
            game_text="Each play can't play any Pok\u00e9mon from his or her hand to evolve his or her Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=AncientPowerPassive(),
        ),
        Attack(
            title="Rock Slide",
            game_text="Does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=snipe_attack(10, pool="bench", count=2, also_base=True),
        ),
    ],
)
