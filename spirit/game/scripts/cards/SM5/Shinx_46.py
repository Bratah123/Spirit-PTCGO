from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy

card = PokemonCardDef(
    guid="d33f1e04-f1d0-5dc6-bdf0-f3ce27e7c7e3",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=403,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_attach_energy(predicate=is_lightning_energy, count=1, to_self=True),
        ),
    ],
)