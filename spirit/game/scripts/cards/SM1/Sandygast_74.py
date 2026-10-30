from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.attacks_common import condition_attack


def _is_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


card = PokemonCardDef(
    guid="bafce824-63b7-55d7-a02b-1ad280869863",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic", "Sandygast"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=769,
    abilities=[
        Attack(
            title="Shore Up",
            game_text="Attach a Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(predicate=_is_fighting_energy, count=1, target='self', prompt='Choose a Fighting Energy card to attach'),
        ),
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)