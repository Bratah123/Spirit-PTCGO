from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rewind_beam
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="e036ce6b-d233-5115-b93f-95f50b4c0e73",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Turn Back Time",
            game_text="If your opponent's Active Pok\u00e9mon is an evolved Pok\u00e9mon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=rewind_beam,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)