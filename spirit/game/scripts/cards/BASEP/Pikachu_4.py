from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import has_energy_cards_attached
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy


card = PokemonCardDef(
    guid="8ce59c3b-4058-58ab-ab41-68764a949a9c",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Recharge",
            game_text="Search your deck for a Lightning Energy card and attach it to Pikachu. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=search_attach_energy(
                predicate=is_lightning_energy, count=1, to_self=True,
                prompt="Choose a Lightning Energy card to attach to Pikachu.",
            ),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Pikachu in order to use this attack.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=50,
            condition=has_energy_cards_attached(),
            effect=self_energy_discard_attack(all_energy=True, before_damage=True),
        ),
    ],
)
