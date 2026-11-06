from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_energy_card

card = PokemonCardDef(
    guid="c539ebaf-8b8b-5ae1-8efb-d74c84575217",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="BW2",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(
                predicate=lambda c: is_energy_card(c) and energy_provides_type(
                    c, PokemonTypes.LIGHTNING.value
                ),
                to_self=True,
                prompt="Choose a Lightning Energy card to attach.",
            ),
        ),
        Attack(
            title="Disaster Volt",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=self_energy_discard_attack(1),
        ),
    ],
)
