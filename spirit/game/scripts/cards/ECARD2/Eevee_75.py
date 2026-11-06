from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import search_attach_energy


card = PokemonCardDef(
    guid="167e4a3d-8cc5-5696-866d-2403ae1250ba",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Charge Up",
            game_text="Flip a coin. If heads, search your deck for an Energy card and attach it to Eevee. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=search_attach_energy(to_self=True)),
        ),
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)
